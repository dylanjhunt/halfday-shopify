import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const cwd = fileURLToPath(new URL('../', import.meta.url));
const status = spawnSync('git', ['status', '--porcelain'], { cwd, encoding: 'utf8' });
if (status.status !== 0 || status.stdout.trim()) {
  console.error('Commit or stash local changes before pulling the live Shopify theme.');
  process.exit(1);
}
const result = spawnSync('shopify', ['theme', 'pull', '--store', 'halfday-tonics.myshopify.com', '--live'], { cwd, stdio: 'inherit' });
process.exit(result.status ?? 1);
