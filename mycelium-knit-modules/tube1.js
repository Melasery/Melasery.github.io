
 
const knitout = require('knitout');
k = new knitout.Writer({carriers:['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']});

 
k.addHeader('Machine','SWGXYZ');
k.addHeader('Gauge','15');
const Carrier = '5';
const carrier2= '6';

k.inhook(Carrier);
for(var i=41;i>0;i--){
    k.tuck("-","f"+i,Carrier);
    i--;
    k.tuck("-","b"+i,Carrier);
}
for(var i=0;i<41;i++){
    k.tuck("+","f"+i,Carrier);
    i++;
    k.tuck("+","b"+i,Carrier);
}
k.releasehook(Carrier);


for(var h=0; h <= 10; h++){

    for(var i= 41; i >= 0; i--){
        k.knit("-", "f" + i, Carrier)
    }
    for(var i=0; i<= 41; i++){
        k.knit("+", "b" + i, Carrier)
    }
}

for(var i=10; i<= 30; i++){
    k.xfer("b" + i, "f" +i)
}

for(var i= 41; i>= 10; i--){
    k.knit("-" , "f" + i, Carrier)
}
for(var i = 10; i <= 41; i++ ){
    k.knit("+", "f" + i, Carrier)
}

k.inhook(carrier2);

for(var i= 30; i>= 0; i--){
    k.knit('-', 'f' + i, carrier2)
}
k.releasehook(carrier2);

for(var i= 11; i <= 29; i++){
    k.drop("f" + i);
}

for(var h=0; h <= 10; h++){

    for(var i= 41; i >= 30; i--){
        k.knit("-", "f" + i, Carrier)
    }
    for(var i=31; i<= 41; i++){
        k.knit("+", "b" + i, Carrier)
    }
    for(var i=0; i<= 10; i++){
        k.knit("+", "b" + i, carrier2)
    }
    for(var i= 10; i >= 0; i--){
        k.knit("-", "f" + i, carrier2)
    }
}
for(var i= 0; i<= 10; i++){
    k.knit('+', "f" + i, carrier2)
}
for(var i= 11; i<= 41; i++){
    k.knit("+", "f" + i, carrier2)
}
for(var i = 41; i>= 0; i--){
    k.knit("-", "f" + i, carrier2)
}

for(var i= 0; i<= 10; i++){
    k.knit('+', "f" + i, carrier2)
}


for(var i= 11; i<= 30; i++){
    k.knit('+', "f" + i, carrier2);
    i ++;
    k.knit('+', 'b' + i, carrier2);
}

for(var i= 30; i>= 11; i--){
    k.knit('-', 'f' + i, carrier2);
    i --;
    k.knit('-', 'b' + i, carrier2);
}
for(var i= 11; i<= 30 ; i++){
    k.knit('+', "f" + i, carrier2);
    i ++;
    k.knit('+', 'b' + i, carrier2);
}
for(var i= 30; i>= 11; i--){
    k.knit('-', 'f' + i, carrier2);
    i --;
    k.knit('-', 'b' + i, carrier2);
}
for(var i= 10; i >= 0; i--){
    k.knit("-", "b" + i, carrier2);
}

for(var h=0; h <= 20; h++){
    for(var i=0; i<= 41; i++){
        k.knit("+", "f" + i, carrier2)
    }
    for(var i= 41; i >= 0; i--){
        k.knit("-", "b" + i, carrier2)
    }

    
}

for (let n = 0; n <= 41; ++n) {
	k.drop("f" + n);
}
for (let n = 0; n <= 41; ++n) {
	k.drop("b" + n);
}






k.outhook(carrier2);
k.outhook(Carrier);

k.write('hole.k');