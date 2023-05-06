import * as mod from './module.js'

mod.email.addEventListener('input', mod.verifyEmail);
mod.password.addEventListener('input', mod.verifyPassword);

mod.myCommunityForm.addEventListener('input', () => {
    if ((mod.emailPattern.test(mod.email.value)) && (mod.password.value.length >= 5)) {
        mod.submitButton.removeAttribute("disabled")
    } else {
        mod.submitButton.setAttribute("disabled", "disabled")
    }
});

function validateLogin() {
    if (!(mod.emailPattern.test(mod.email.value))) {
        mod.email.focus();
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    if (password.value === '' || password.value === null) {
        mod.password.focus()
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    return true;
}