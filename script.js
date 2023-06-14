function Log(){
	let Target = parseFloat(document.getElementById("Target").value);
	let Projectile = parseFloat(document.querySelector('input[name="Projectile"]:checked').value);
	let Angle = Math.PI*(document.getElementById('range').value/180)
	let K = ((Math.sqrt((Target**2)-((Projectile**2)*Math.sin(Angle))) + (Projectile*Math.cos(Angle)))/(Target + Projectile))**2
	console.log(K)
	factorK.innerHTML = `<p>${K}</p>`;


}




//Slider
const
  range = document.getElementById('range'),
  rangeV = document.getElementById('rangeV'),
  setValue = ()=>{
    const
      newValue = Number( (range.value - range.min) * 100 / (range.max - range.min) ),
      newPosition = 10 - (newValue * 0.2);
    rangeV.innerHTML = `<span>${range.value}</span>`;
    rangeV.style.left = `calc(${newValue}% + (${newPosition}px))`;
  };
document.addEventListener("DOMContentLoaded", setValue);
range.addEventListener('input', setValue);