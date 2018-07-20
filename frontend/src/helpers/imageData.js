export default function getImageData() {
  const unparsedData = document.querySelector("#imagedata");
  return JSON.parse(unparsedData.innerText).images;
}
