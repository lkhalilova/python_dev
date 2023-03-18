// 1
const myDiv = document.createElement("div");
myDiv.className = "buttons";
myDiv.style.textAlign = "center";
["Add a friend", "Message", "Offer a job"].map(buttonName => {
    let button = document.createElement("button");
    button.innerText = buttonName;
    button.style.background = "orange"
    myDiv.appendChild(button);
});

document.getElementsByTagName("body")[0].appendChild(myDiv);

// 5
let hide_button = document.getElementsByTagName("button")[1];
hide_button.style.display = "none";
let job = document.getElementsByTagName("button")[3];
count = 0;
job.onclick = function (event) {
    let click_count = ++count;
    if (count % 2 === 0) {
       hide_button.style.display = "inline";
    } else {
        hide_button.style.display = "none";
    }
};


// 2, 3
let random_friends_number = document.getElementById("4");
let num = Math.floor(Math.random() * 100);
random_friends_number.textContent = num.toString();

let add_friend = document.getElementsByTagName("button")[1];
let button_friends = document.getElementById("4");
add_friend.onclick = (event) => {
    let current_number = parseInt(button_friends.textContent);
    let new_number = current_number += 1;
    button_friends.textContent = new_number.toString();
    add_friend.innerText = "waiting for confirmation";
    add_friend.disabled = true;
};

// 4
let dm = document.getElementsByTagName("button")[2];
function color_change() {
    if (dm.style.background === "orange") {
        dm.style.background = "blue";
    } else {
        dm.style.background = "orange";
    }
}

dm.onclick = (event) => color_change();

// 6
const newDiv = document.createElement("div");
newDiv.style.textAlign = "center";
let hm = document.createElement("button");
hm.innerText = "submit a homework";
hm.style.background = "red";
hm.style.margin = "20px"
newDiv.appendChild(hm);

document.getElementsByTagName("body")[0].appendChild(newDiv);

let hm_submit = document.getElementsByTagName("button")[4];

hm_submit.onclick = (event) => {
    const tr = document.createElement("tr");
    ["14", "27", "in process"].map(text => {
        let td = document.createElement("td");
        td.innerText = text;
        tr.appendChild(td);
});
document.getElementsByTagName("tbody")[0].appendChild(tr);
};