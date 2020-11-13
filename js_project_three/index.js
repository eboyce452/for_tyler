var circles = [
	document.getElementById('circle_one'),
	document.getElementById('circle_two'),
	document.getElementById('circle_three'),
	document.getElementById('circle_four'),
	document.getElementById('circle_five'),
];

for (var i = 0; i < circles.length; i++){
	circles[i].className = 'true';
}

console.log('connected');
console.log('');

var circle_states = [
	true,
	true,
	true,
	true,
	true,
]

async function collision_detection(collision_object){
	var is_a_circle = circles.includes(collision_object);
	if (is_a_circle == true){
		collision_object.className = 'false';
		circle_states[circles.indexOf(collision_object)] = false;
	
		if (circle_states.every(check_for_all_false) === true){
			for (var x = 0; x < circle_states.length; x++){
				circle_states[x] = true;
				await new Promise(r => setTimeout(r, 200));
				circles[x].className = 'true'
			}
		}
	}
}

function check_for_all_false(boolean_val){
	return boolean_val === false;
}

var handler = function(){
	collision_detection(event.target);
}

document.addEventListener('mouseover', handler);

// Here is the best I can do for a step by step explanation:
// If the above code looks complicated, it's because of all the visual components as opposed to the necessary logic to accomplish what you are looking for

// var circles = [obj1,obj2,obj....] contains the objects that you're checking collisions for.

// var circle_states = [true,true,true,true,true,]; initializes your array with 5 booleans all equal to true
// function collision_detection(collision_object){...} is a function that passes in the target of an event and contains the logic that will handle the rest of your needs

// var is_a_circle determines whether the object passed into the function matches one of the objects you care about
// if (is_a_circle == true){...} says that if it is an object you care about, then go ahead and change its state

// In this case, I know which circle I mouse over because I have an array with all the circle objects and the collision_object will match the index of one of those circles in the var circles array.
// With that array position, I can then change the corresponding state in var circle_states to false (meaning a dead object)

// Lastly, you have an if statement after changing the state of the most recent circle that checks the state of all the circles. There are a ton of expressions in every language that can do this. 
// In JS, because it's the enemy, you create a condition as the return of a function where you pass in an array item to check. Then you do array.every(function) and it will pass in each array item,
// evaluate it, and then return a boolean depending on if they all meet the condition or not. It's heinous.

// If for some reason your language doesn't have that kind of statement you can code it like this:
// var all_false = true;
// for (var j = 0; j < circle_states.length; j++){
//		if (circle_states[j] == true){
//			all_false = false;
// 		}
// }

// So if there is a single true boolean in the entire array, all_false will be set to false. Otherwise it will remain true and then you can feed that variable into if (all_false == true){etc...}
// The for loop inside if (all_false == true){...} just iterates through the array and reassigns all the values to true and the whole thing starts anew.

// The whole thing could be coded much more cleanly, but I wanted to make it as readable as possible, even if it's kind of repetitive.