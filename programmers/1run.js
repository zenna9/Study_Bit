function solution(players, callings) {

    // for(let k=0 ;k<callings.length;k++ ){
    //     let callindex = players.indexOf(callings[k]);
    //     players.splice(callindex, 1 );
    //     players.splice(callindex-1, 0, callings[k]);
    // }
    // for(let c =0 ; c < callings.length ; c++) {
    //     // console.log("callings : "+callings[c]);
    //     for(let p = 0 ; p < players.length ; p++){
    //         // console.log("players : " +p)
    //         // console.log(players[p], callings[c]);
    //         if(players[p]==callings[c]){
    //             let oldwinner = players[p-1];
    //             players.splice(p-1,2, players[p],oldwinner);
    //             break;
    //         }
    //     }
    // }

    let counters = {};
    callings.forEach(i => {
        let thisi = counters[i];
        if(thisi == undefined){
            counters[i] = 1;
        }else{
            counters[i] += 1;
        }
    });

    // Object.keys(counters).forEach((ite)=>{
        
    //     let front = players.slice(0, );
    //     let back = [];
    //     console.log(players.indexOf(ite));

    // })
    let newplayers = [];
    Object.keys(counters).forEach((ckey)=>{
        let ckeyIndex = players.indexOf(ckey);
        for (let i = 0; i < players.length; i++){
            const element = players[i];
    
            
        }
    })
    // return newplay;
}
console.log(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]));