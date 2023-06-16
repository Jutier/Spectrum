function Calculate(){
	let Target = document.getElementById("Target").value;
	let M2 = AtomMass[Target];
	let Projectile = document.querySelector('input[name="Projectile"]:checked').value;
	let M1 = AtomMass[Projectile];
	let Angle = Math.PI*(document.getElementById('range').value/180);
	let MR = M1/M2;
	let K = ((Math.sqrt(1-(MR**2)*Math.sin(Angle)**2) + MR*Math.cos(Angle))/(1+MR))**2;
	let Kround = Math.round(K*10000)/10000;
	factorK.innerHTML = `<p>${Kround}</p>`;
	console.log(M2, M1)


}




// Slider
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
//