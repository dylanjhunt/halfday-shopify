/* Decorative media sources stay in an inert template until the card is visible. */
if (!customElements.get('halfday-video')) {
  class HalfdayVideo extends HTMLElement {
    constructor() {
      super();
      this.update = this.update.bind(this);
    }

    connectedCallback() {
      if (this.observer || !('IntersectionObserver' in window)) return;
      this.motion = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.observer = new IntersectionObserver(([entry]) => {
        this.visible = entry.isIntersecting && entry.intersectionRatio >= 0.1;
        this.update();
      }, { threshold: 0.1 });
      this.observer.observe(this);
      this.motion.addEventListener('change', this.update);
      document.addEventListener('visibilitychange', this.update);
    }

    update() {
      const shouldPlay = this.visible && !this.motion.matches && !document.hidden;
      if (!shouldPlay) {
        this.video?.pause();
        this.removeAttribute('playing');
        return;
      }
      if (!this.video) {
        const template = this.querySelector('template');
        if (!template) return;
        this.video = template.content.querySelector('video').cloneNode(true);
        this.video.muted = true;
        this.video.addEventListener('playing', () => {
          if (this.visible && !this.motion.matches && !document.hidden) {
            this.setAttribute('playing', '');
          } else {
            this.video.pause();
          }
        });
        this.video.addEventListener('error', () => this.removeAttribute('playing'));
        this.appendChild(this.video);
      }
      this.video.play().catch(() => this.removeAttribute('playing'));
    }

    disconnectedCallback() {
      this.video?.pause();
      this.observer?.disconnect();
      this.motion?.removeEventListener('change', this.update);
      document.removeEventListener('visibilitychange', this.update);
      this.observer = null;
    }
  }
  customElements.define('halfday-video', HalfdayVideo);
}
