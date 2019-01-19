function highAndLow(numbers){
    const splitNumbers = numbers.split(" ");
    let maxx = -Number.MAX_SAFE_INTEGER;
    let minn = Number.MAX_SAFE_INTEGER;
    
    for (let i = 0; i < splitNumbers.length; ++i) {
        const nrInt = parseInt(splitNumbers[i]);
        if (nrInt > maxx) {
            maxx = nrInt;
        } 
        if (nrInt < minn) {
            minn = nrInt;
        }
    }
    
    return maxx + " " + minn;
}