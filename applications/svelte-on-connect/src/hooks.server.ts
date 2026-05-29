import type { Handle } from '@sveltejs/kit';
import type { User } from '$lib/models/user';

export const handle: Handle = async ({ event, resolve }) => {
	// Get the user from Posit Connect
	const connectCredentials = event.request.headers.get('rstudio-connect-credentials');
	if (connectCredentials) {
		try {
			event.locals.user = JSON.parse(connectCredentials) as User;
		} catch {
			event.locals.user = null;
		}
	} else {
		event.locals.user = null;
	}

	const response = await resolve(event);
	return response;
};
