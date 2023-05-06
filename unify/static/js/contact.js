const contactForm = document.forms['contact-form'];
const subject = document.forms['contact-form']['subject'];
const message = document.forms['contact-form']['message'];
const submitBTN = document.getElementById('submit');

contactForm.addEventListener('input', () => {
    if (subject.value.trim() && message.value.trim()) {
        submitBTN.removeAttribute("disabled")
    } else {
        submitBTN.setAttribute("disabled", "disabled");
    }
});

function contactFormHandler() {
    if (!subject.value.trim()) {
        submitBTN.addEventListener('submit', e => e.preventDefault())
        return false
    }
    if (!message.value.trim()) {
        submitBTN.addEventListener('submit', e => e.preventDefault())
        return false
    }
    return true
}