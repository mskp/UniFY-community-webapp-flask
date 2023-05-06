let postForm = document.forms['post-form']
let inputPost = document.getElementById('post');
let inputPhoto = document.getElementById('photo')
let postButton = document.getElementById('post-btn');

postForm.addEventListener("input", () => {
    if (inputPost.value.trim() || inputPhoto.value.trim()) {
        postButton.removeAttribute("disabled");
    } else {
        postButton.setAttribute("disabled", "disabled");
    }
});

// const compressImage = () => {
//     const file = inputPhoto.files[0];
    
//     if (!file) return;

//     let reader = new FileReader();
//     reader.readAsDataURL(file);
//     reader.onload = (e) => {
//         let imageElement  = document.createElement("img");
//         imageElement.src = e.target.result;
//         inputPhoto.src = e.target.result;

//         imageElement.onload = (e) => {
//             const canvas = document.createElement("canvas");
//             const MAX_WIDTH = 400;

//             const scaleSize = MAX_WIDTH / e.target.width;
//             canvas.width = MAX_WIDTH;
//             canvas.height = e.target.height *scaleSize;
//             const context = canvas.getContext("2d");
//             context.drawImage(e.target, 0, 0, canvas.width, canvas.height);
//             const srcEncoded = context.canvas.toDataURL(e.target, "imaeg/jpeg");
//             document.querySelector('#output').src = srcEncoded;
//         }
//     }
// }