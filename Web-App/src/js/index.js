var vph = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

// Guarantees the dots image container extends to the full viewport height.
var oldPadding = parseInt($("#dots-container").css("padding-top"));
var newPadding = Math.floor((vph-72-636)/2);
if (newPadding > 0) {
    $("#dots-container").css("padding-top", oldPadding + newPadding + "px");
    $("#dots-container").css("padding-bottom", oldPadding + newPadding + "px");
}
