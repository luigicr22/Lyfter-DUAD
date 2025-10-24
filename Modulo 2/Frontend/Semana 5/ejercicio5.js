// Entrada
function infoStudent (student){
    try{
        const studentInfo = {name: student.name, gradeAvg: 0, highestGrade: {}, lowestGrade: {}};
        if (student.grades.length > 0){
            studentInfo.highestGrade = student.grades[0];
            studentInfo.lowestGrade = student.grades[0];
            for (const note of student.grades){
                if (note.grade > studentInfo.highestGrade.grade){
                    studentInfo.highestGrade = note;
                }
                if (note.grade < studentInfo.lowestGrade.grade){
                    studentInfo.lowestGrade = note;
                }
                studentInfo.gradeAvg += note.grade;
            }
            studentInfo.gradeAvg = (studentInfo.gradeAvg/student.grades.length);
            studentInfo.highestGrade = studentInfo.highestGrade.name;
            studentInfo.lowestGrade = studentInfo.lowestGrade.name;
        }
        else {
            throw ("Objeto sin registro de notas")
        }
        return studentInfo;
    }
    catch (e){
        console.log(e)
    }
}

const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	],
}

const result = infoStudent(student);
console.log(result);

