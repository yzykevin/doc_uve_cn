// Trigger the Read the Docs Addons Search modal when clicking on "Search docs" input from the topnav.
document.querySelector("[role='search'] input").addEventListener("focusin", () => {
   const event = new CustomEvent("readthedocs-search-show");
   document.dispatchEvent(event);
});

// Read the Docs uses clean URLs, while the Sphinx theme emits relative
// links such as ../index.html. Normalize the home links to the version root.
(() => {
   const canonical = document.querySelector("link[rel='canonical']");
   if (!canonical) return;
   const canonicalUrl = new URL(canonical.href, window.location.href);
   const marker = "/content_en/";
   const markerIndex = canonicalUrl.pathname.indexOf(marker);
   if (markerIndex >= 0) {
      canonicalUrl.pathname = `${canonicalUrl.pathname.slice(0, markerIndex)}/`;
   } else {
      canonicalUrl.pathname = canonicalUrl.pathname.replace(/\/index\.html$/, "/");
   }
   canonicalUrl.search = "";
   canonicalUrl.hash = "";
   document.querySelectorAll("a.icon-home").forEach((link) => {
      link.href = canonicalUrl.href;
   });
})();
