const search_boxes = Array.from(document.getElementsByTagName('input'));
search_boxes.forEach(element => {
    element.addEventListener('click' , () => {
        const icon = element.parentElement.querySelector('svg');
        icon.style.opacity = 0;
    })

    element.addEventListener('keydown' , (event) => {
        if(event.key === 'Enter') {
            const icon = element.parentElement.querySelector('svg');
            icon.style.opacity = 1;
            element.value = "";
            if(element.id === 'location-search') {
                element.placeholder = "                SVNIT surat , piplod";
            }
            else {
                element.placeholder = "             Serch for a restaurant or a dish..."
            }
        }
    })
});

