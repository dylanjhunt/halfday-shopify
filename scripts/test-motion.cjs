// Exercise the motion lifecycle without browser, app or customer sessions.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(new URL('../assets/custom.js', `file://${__filename}`), 'utf8');
const motionSource = source.slice(source.indexOf('const halfdayMotion ='), source.indexOf('function halfdaySwiper'));
function events(extra = {}) {
  const handlers = {};
  return Object.assign(extra, {
    addEventListener(name, handler) { (handlers[name] ||= []).push(handler); },
    emit(name, event = {}) { (handlers[name] || []).forEach(handler => handler(event)); }
  });
}
const element = events({ dataset: {}, contains: node => node === element });
const page = events({ hidden: false, querySelectorAll: () => [element] });
const preference = events({ matches: false });
let observer, created = 0, destroyed = 0;
const states = [];
class Observer {
  constructor(callback) { this.callback = callback; observer = this; }
  observe(target) { this.target = target; }
  unobserve(target) { assert.equal(target, element); this.target = null; }
  visible(value) { this.callback([{ target: element, isIntersecting: value, intersectionRect: { width: value ? 300 : 0 } }]); }
}
const register = vm.runInNewContext(`${motionSource}; halfdayMotion`, {
  document: page, window: { matchMedia: () => preference, IntersectionObserver: Observer }, IntersectionObserver: Observer
});
register('.test-carousel', () => {
  created++;
  return { setRunning: state => states.push(state), destroy: () => destroyed++ };
});
assert.equal(created, 0, 'offscreen content must not initialize');
observer.visible(true);
assert.equal(created, 1);
assert.equal(states.at(-1), true);
element.emit('focusin');
assert.equal(states.at(-1), false, 'keyboard focus pauses motion');
element.emit('focusout', { relatedTarget: element });
assert.equal(states.at(-1), false, 'focus within the carousel keeps it paused');
element.emit('focusout', { relatedTarget: null });
assert.equal(states.at(-1), true);
page.hidden = true; page.emit('visibilitychange');
assert.equal(states.at(-1), false, 'background tabs must pause');
page.hidden = false; page.emit('visibilitychange');
assert.equal(states.at(-1), true);
preference.matches = true; preference.emit('change');
assert.equal(states.at(-1), false, 'reduced motion must pause autoplay');
observer.visible(false); observer.visible(true);
assert.equal(states.at(-1), false, 'scrolling must not override reduced motion');
preference.matches = false; preference.emit('change');
assert.equal(states.at(-1), true);
observer.visible(false);
assert.equal(states.at(-1), false, 'offscreen content must pause');
assert.equal(created, 1, 'returning to view must reuse the instance');
page.emit('shopify:section:unload', { target: { contains: node => node === element } });
assert.equal(destroyed, 1, 'editor unload must destroy the instance');
assert.equal(observer.target, null);
console.log('Motion lifecycle passed: lazy initialization, focus, visibility, reduced motion, reuse and editor cleanup.');
