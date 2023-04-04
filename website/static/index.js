function deletgroupe(goupeId){
    fetch('/delete-groupe', {
        method: 'POST',
        body: JSON.stringify({groupeId: groupeId})
    }).then((_res) => {
        window.location.href = "/";
    })
}