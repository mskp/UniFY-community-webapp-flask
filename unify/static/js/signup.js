import * as mod from './module.js';

mod.fullname.addEventListener('input', () => {
    if (mod.fullname.value === '' || mod.fullname.value.length < 4 || mod.fullname.value.length > 20) {
        mod.nameSpan.style.setProperty("--span-color", "red")
        mod.nameLabel.style.color = "red";
        mod.fullname.focus();
    } else {
        mod.nameSpan.style.setProperty("--span-color", "green")
        mod.nameLabel.style.color = "green";
    }
});
mod.email.addEventListener('input', mod.verifyEmail);
mod.password.addEventListener('input', mod.verifyPassword);
mod.confirmPassword.addEventListener('input', mod.verifyPassword);

mod.myCommunityForm.addEventListener('input', () => {
    if ((mod.fullname.value.length >= 4) && (mod.emailPattern.test(mod.email.value)) && (mod.password.value.length >= 5) && (mod.password.value === mod.confirmPassword.value)) {
        mod.submitButton.removeAttribute("disabled")
    } else {
        mod.submitButton.setAttribute("disabled", "disabled")
    }
});

function validateSignup() {
    if (mod.namePattern.test(mod.fullname.value) || mod.fullname.value === '') {
        mod.fullname.focus();
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    if (!(mod.emailPattern.test(email.value)) || mod.email.value === '') {
        mod.email.focus();
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    if (mod.password.value === '' || mod.password.value === null) {
        mod.password.focus();
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    if (mod.confirmPassword.value === '' || mod.confirmPassword.value === null || mod.confirmPassword.value !== password.value) {
        mod.confirmPassword.focus();
        mod.submitButton.addEventListener('submit', e => e.preventDefault());

        return false;
    }
    return true;
}
