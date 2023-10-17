const masonryBtn = document.getElementById("masonry-btn");
// const listBtn = document.getElementById("list-btn");
const stdBtn = document.getElementById("std-btn");

const masonryView = document.getElementById('masonry-view');
// const listView = document.getElementById('list-view');
const stdView = document.getElementById('std-view');

updateDisplayMode();

function setDisplayMode(displayMode) {
    localStorage.setItem('displayMode', displayMode);
}

function getDisplayMode() {
    return localStorage.getItem('displayMode');
}

function updateDisplayMode() {
    const currentDisplayMode = getDisplayMode() || 'masonry'; 
    switch (currentDisplayMode) {
        case 'masonry':
            setMasonryView();
            masonryBtn.style.display = "";
            // listBtn.style.display = "none";
            stdBtn.style.display = "none";
            masonryView.style.display = "";
            // listView.style.display = "none";
            stdView.style.display = "none";
            break;
        // case 'list':
        //     masonryBtn.style.display = "none";
        //     listBtn.style.display = "";
        //     stdBtn.style.display = "none";
        //     masonryView.style.display = "none";
        //     listView.style.display = "";
        //     stdView.style.display = "none";
        //     break;
        case 'standard':
            masonryBtn.style.display = "none";
            // listBtn.style.display = "none";
            stdBtn.style.display = "";
            masonryView.style.display = "none";
            // listView.style.display = "none";
            stdView.style.display = "";
            break;
        default:
            break;
    }
}

// Switch to the next mode
masonryBtn.addEventListener("click", () => {
    setDisplayMode('standard');
    updateDisplayMode();
});

// listBtn.addEventListener("click", () => {
//     setDisplayMode('standard');
//     updateDisplayMode();
// });

stdBtn.addEventListener("click", () => {
    setDisplayMode('masonry'); 
    updateDisplayMode();
});


function setMasonryView() {
    // Initialize Masonry
    var masonryGrid = document.getElementById("masonry-view");
    var masonry = new Masonry(masonryGrid, {
        percentPosition: true, 
    });

    // Initialize ImagesLoaded
    var imgLoad = imagesLoaded(masonryGrid);

    // When all images are loaded, relayout Masonry
    imgLoad.on("always", function () {
        masonry.layout();
    });
}

// Instrument badge settings
const instrumentLanguage = document.querySelector("#instrument-language-element");
const instrumentBadge = document.querySelector("#instrument-language-badge");

updateInstrumentBadge();

function updateInstrumentBadge() {
    const hideInstrumentBadge = localStorage.getItem('hideInstrumentBadge') || false;
    if (hideInstrumentBadge) {
        instrumentBadge.style.display = "none";
    } else {
        instrumentBadge.style.display = "";
    }
}

instrumentLanguage.addEventListener("click", function () {
    localStorage.setItem("hideInstrumentBadge", true);
    updateInstrumentBadge();
});