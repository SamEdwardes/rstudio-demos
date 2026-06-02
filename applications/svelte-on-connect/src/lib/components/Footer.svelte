<script lang="ts">
	import { resolve } from '$app/paths';

	const year = new Date().getFullYear();

	const navLinks = [
		{ href: '/dashboard', label: 'Dashboard' },
		{ href: '/reports', label: 'Reports' },
		{ href: '/settings', label: 'Settings' }
	] as const;
</script>

<footer class="border-t border-gray-200 bg-white">
	<div class="mx-auto max-w-6xl px-4 py-10">
		<div class="grid grid-cols-2 gap-8 sm:grid-cols-4">
			<div class="col-span-2 sm:col-span-1">
				<p class="text-base font-semibold text-gray-900">Svelte on Connect</p>
				<p class="mt-2 text-sm text-gray-500">A placeholder tagline goes here.</p>
			</div>
			<div>
				<p class="text-sm font-semibold text-gray-900">Navigation</p>
				<ul class="mt-3 space-y-2 text-sm">
					{#each navLinks as { href, label } (href)}
						<li>
							<a href={resolve(href)} class="text-gray-500 hover:text-gray-900">{label}</a>
						</li>
					{/each}
				</ul>
			</div>
			<div>
				<p class="text-sm font-semibold text-gray-900">Resources</p>
				<ul class="mt-3 space-y-2 text-sm">
					<li>
						<a href="https://svelte.dev/docs/svelte" class="text-gray-500 hover:text-gray-900">
							Svelte docs
						</a>
					</li>
					<li>
						<a href="https://svelte.dev/docs/kit" class="text-gray-500 hover:text-gray-900">
							SvelteKit docs
						</a>
					</li>
					<li>
						<a href="https://docs.posit.co/connect/" class="text-gray-500 hover:text-gray-900">
							Posit Connect
						</a>
					</li>
				</ul>
			</div>
		</div>
		<p class="mt-10 border-t border-gray-100 pt-6 text-sm text-gray-500">
			&copy; {year} Svelte on Connect. All rights reserved.
		</p>
	</div>
</footer>
