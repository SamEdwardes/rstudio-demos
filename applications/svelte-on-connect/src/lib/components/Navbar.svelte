<script lang="ts">
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { type User } from '$lib/models/user';

	interface Props {
		user: User | null;
	}

	let { user = null }: Props = $props();

	const initial = $derived(user?.user?.charAt(0).toUpperCase() ?? '');

	const links = [
		{ href: '/', label: 'Home' },
		{ href: '/dashboard', label: 'Dashboard' },
		{ href: '/reports', label: 'Reports' },
		{ href: '/settings', label: 'Settings' }
	] as const;

	function isActive(href: string): boolean {
		const id = page.route.id;
		if (!id) return false;
		return href === '/' ? id === '/' : id === href || id.startsWith(`${href}/`);
	}
</script>

<header class="sticky top-0 z-10 border-b border-gray-200 bg-white/80 shadow-sm backdrop-blur">
	<nav class="mx-auto flex h-16 max-w-6xl items-center justify-between gap-8 px-6">
		<a href={resolve('/')} class="flex items-center gap-2.5 text-gray-900">
			<span
				class="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-sm font-bold text-white"
			>
				S
			</span>
			<span class="text-lg font-semibold tracking-tight">Svelte on Connect</span>
		</a>
		<div class="flex items-center gap-4">
			<ul class="flex items-center gap-1 text-sm font-medium">
				{#each links as { href, label } (href)}
					<li>
						<a
							href={resolve(href)}
							aria-current={isActive(href) ? 'page' : undefined}
							class="rounded-md px-3 py-2 transition-colors {isActive(href)
								? 'bg-blue-50 text-blue-700'
								: 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'}"
						>
							{label}
						</a>
					</li>
				{/each}
			</ul>
			{#if user}
				<div
					class="flex items-center gap-2 border-l border-gray-200 pl-4"
					title={user.groups.join(', ')}
				>
					<span
						class="flex h-8 w-8 items-center justify-center rounded-full bg-gray-200 text-sm font-semibold text-gray-700"
					>
						{initial}
					</span>
					<span class="text-sm font-medium text-gray-700">{user.user}</span>
				</div>
			{/if}
		</div>
	</nav>
</header>
