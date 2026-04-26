function switchMode(mode) {
	const parent = document.getElementById('form-parent');
	const signupForm = document.getElementById('signup-form');
	const loginForm = document.getElementById('login-form');
	const signupTab = document.getElementById('tab-signup');
	const loginTab = document.getElementById('tab-login');

	if (mode === 'login') {
		parent.classList.add('show-login-state');

		// Hide/Show logic
		signupForm.classList.add('hidden');
		loginForm.classList.remove('hidden');

		// Active tab styling
		loginTab.classList.add('active');
		signupTab.classList.remove('active');
	} else {
		parent.classList.remove('show-login-state');

		loginForm.classList.add('hidden');
		signupForm.classList.remove('hidden');

		signupTab.classList.add('active');
		loginTab.classList.remove('active');
	}
}
