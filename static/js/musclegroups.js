function updateMuscleGroup() {
    var exerciseSelect = document.getElementById("id_exercise");
    var selectedExercise = exerciseSelect.options[exerciseSelect.selectedIndex].text;
    var muscleGroupInput = document.getElementById("muscle_group");

    // You might want to use an AJAX call to fetch the muscle group based on the selected exercise
    var muscleGroups = {
  
        'Squat': 'Legs',
        'Bicep Curl': 'Arms',
        'Plank': 'Core',
        'Deadlift': 'Back',
        'Shoulder Press': 'Shoulders',
        'Lateral Raise': 'Shoulders',
        'Leg Press': 'Legs',
        'Tricep Dip': 'Arms',
        'Kettlebell Swing': 'Legs',
        'Russian Twist': 'Core',
        'Push-up': 'Chest',
        'Running': 'Legs',
        'Cycling': 'legs',
        'Swimming': 'Legs',



    };

    muscleGroupInput.value = muscleGroups[selectedExercise] || '';
}