export const myCommunityForm = document.getElementById('mycommunity-form');
export const fullname = document.forms['mycommunity-form']['name'];
export const email = document.forms['mycommunity-form']['email'];
export const password = document.forms['mycommunity-form']['password'];
export const confirmPassword = document.forms['mycommunity-form']['c-password'];
export const submitButton = document.getElementById('submit');
export const nameLabel = document.getElementById('label-name');
export const emailLabel = document.getElementById('label-email');
export const passwordLabel = document.getElementById('label-password');
export const confirmPasswordLabel = document.getElementById('label-cpassword');
export const nameSpan = document.getElementById("name-span");
export const emailSpan = document.getElementById("email-span");
export const passwordSpan = document.getElementById("password-span");
export const confirmPasswordSpan = document.getElementById("cpassword-span");

export const namePattern = /^[A-Za-z]{2,25}$/
export const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
export const passwordPattern = /^\w{6, 20}$/

export function verifyEmail() {
    if (!(emailPattern.test(email.value))) {
        emailSpan.style.setProperty("--span-color", "red")
        emailLabel.style.color = "red";
        email.focus();
    } else {
        emailSpan.style.setProperty("--span-color", "green")
        emailLabel.style.color = "green";
    }
}

export function verifyPassword() {
    if (password.value === "" || password.value === null || password.value.length < 5 || password.value.length > 20) {
        passwordLabel.style.color = "red";
        passwordSpan.style.setProperty("--span-color", "red")
        password.focus();
    } else {
        passwordSpan.style.setProperty("--span-color", "green")
        passwordLabel.style.color = "green";
    }
    
    if (confirmPassword) {
        if (password.value !== confirmPassword.value || password.value === '') {
            confirmPasswordSpan.style.setProperty("--span-color", "red")
            confirmPasswordLabel.style.color = "red";
        } else {
            confirmPasswordSpan.style.setProperty("--span-color", "green")
            confirmPasswordLabel.style.color = "green";
        }
    }
}
