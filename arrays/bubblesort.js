
function bubblesort(array){

    for(let i=0;i<array.length-1;i++)
     for(let j=0;j<(array.length-i)-1;j++){
         if(array[j]>array[j+1]){
            let temp=array[j];
            array[j]=array[j+1];
            array[j+1]=temp;
         }
     }
    }
    
    let userinput=prompt("Enter numbers separated by commas (e.g. 4,3,2,1):");
    let array=userinput.split(',').map(Number);
    bubblesort(array);
    console.log(array);
    