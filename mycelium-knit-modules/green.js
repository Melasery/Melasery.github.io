 
const knitout = require('knitout');
k = new knitout.Writer({carriers:['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']});

 
k.addHeader('Machine','SWGXYZ');
k.addHeader('Gauge','15');

 
 
 
const MAX_NEEDLE =250;       
const MIN_NEEDLE = 0;         
const SPLIT_START = 125;       
const SPLIT_END = 129;         
const DROP_START = 126;        
const DROP_END = 128;          
const ROWS_SECTION_1 = 177;   
const ROWS_SECTION_2 = 37;    
const ROWS_SECTION_3 = 856;
const Carrier = '1';
const carrier2 = '2';



const OUTPUT_FILE = 'blockgreen.k';
 

k.inhook(Carrier);

 
for(var i = MAX_NEEDLE; i > MIN_NEEDLE; i--){
    k.tuck("-", "f" + i, Carrier);
    i--;
    k.tuck("-", "b" + i, Carrier);
}
for(var i = MIN_NEEDLE; i < MAX_NEEDLE; i++){
    k.tuck("+", "f" + i, Carrier);
    i++;
    k.tuck("+", "b" + i, Carrier);
}

k.releasehook(Carrier);

 
for(var h = 0; h <= ROWS_SECTION_1; h++){
    for(var i = MAX_NEEDLE; i >= MIN_NEEDLE; i--){
        k.knit("-", "f" + i, Carrier);
    }
    for(var i = MIN_NEEDLE; i <= MAX_NEEDLE; i++){
        k.knit("+", "b" + i, Carrier);
    }
}

 
for(var i = SPLIT_START; i <= SPLIT_END; i++){
    k.xfer("b" + i, "f" + i);
}

 
for(var i = MAX_NEEDLE; i >= SPLIT_START; i--){
    k.knit("-", "f" + i, Carrier);
}
for(var i = SPLIT_START; i <= MAX_NEEDLE; i++){
    k.knit("+", "f" + i, Carrier);
}

 
k.inhook(carrier2);
for(var i = MIN_NEEDLE; i <= SPLIT_END; i++){
    k.knit('+', 'f' + i, carrier2);
}
k.releasehook(carrier2);
for(var i = SPLIT_END; i >= SPLIT_START; i--){
        k.knit("-", "f" + i, carrier2);
    }
 
for(var i = DROP_START ; i <= DROP_END; i++){
    k.drop("f" + i);
}

 
for(var h = 0; h <= ROWS_SECTION_2; h++){
    for(var i = MAX_NEEDLE; i >= SPLIT_END ; i--){
        k.knit("-", "f" + i, Carrier);
    }
    for(var i = SPLIT_END + 1; i <= MAX_NEEDLE; i++){
        k.knit("+", "b" + i, Carrier);
    }
    for(var i = SPLIT_START; i >= MIN_NEEDLE; i--){
        k.knit("-", "f" + i, carrier2);
    }
    for(var i = MIN_NEEDLE; i <= SPLIT_START; i++){
        k.knit("+", "b" + i, carrier2);
    }
}

 
for(var i = SPLIT_START; i <= MIN_NEEDLE; i--){
    k.knit('-', "f" + i, carrier2);
}
for(var i = DROP_START + 1; i <= MAX_NEEDLE; i++){
    k.knit("+", "f" + i, carrier2);
}
for(var i = MAX_NEEDLE; i >= MIN_NEEDLE; i--){
    k.knit("-", "f" + i, carrier2);
}
for(var i = MIN_NEEDLE; i <= SPLIT_START; i++){
    k.knit('+', "f" + i, carrier2);
}

 
for(var i = DROP_START; i <= SPLIT_END; i++){
    k.knit('+', "f" + i, carrier2);
    i++;
    k.knit('+', 'b' + i, carrier2);
}
for(var i = SPLIT_END; i >= DROP_START; i--){
    k.knit('-', 'f' + i, carrier2);
    i--;
    k.knit('-', 'b' + i, carrier2);
}
for(var i = DROP_START; i <= SPLIT_END; i++){
    k.knit('+', "f" + i, carrier2);
    i++;
    k.knit('+', 'b' + i, carrier2);
}
for(var i = SPLIT_END; i >= DROP_START; i--){
    k.knit('-', 'f' + i, carrier2);
    i--;
    k.knit('-', 'b' + i, carrier2);
}

 
for(var i = SPLIT_START; i >= MIN_NEEDLE; i--){
    k.knit("-", "b" + i, carrier2);
}

 
for(var h = 0; h <= ROWS_SECTION_3; h++){
    for(var i = MIN_NEEDLE; i <= MAX_NEEDLE; i++){
        k.knit("+", "f" + i, carrier2);
    }
    for(var i = MAX_NEEDLE; i >= MIN_NEEDLE; i--){
        k.knit("-", "b" + i, carrier2);
    }
}





k.outhook(carrier2);
k.outhook(Carrier);

 
for(let n = MIN_NEEDLE; n <= MAX_NEEDLE; ++n){
    k.drop("f" + n);
}
for(let n = MIN_NEEDLE; n <= MAX_NEEDLE; ++n){
    k.drop("b" + n);
}

k.write(OUTPUT_FILE);