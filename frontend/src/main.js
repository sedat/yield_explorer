import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		walletAddress: '0x878BC5bC7cBc369dffC00cdc6e1718478dc1D639',
		author: 'Sedat'
	}
});

export default app;