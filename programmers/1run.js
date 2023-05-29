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

    ////3번째 시도 실패================
    // let counters = {};
    // callings.forEach(i => {
    //     if(counters[i] == undefined){
    //         counters[i] = 1;
    //     }else{
    //         counters[i] += 1;
    //     }
    // });

    // Object.keys(counters).forEach((ite)=>{
    //     let frontplayers = [];  
    //     const indexq = players.indexOf(ite);
    //     const indexx = indexq - counters[ite];
    //     players.map((item, index)=>{
    //         if(index < indexx){
    //             frontplayers.push(item);
    //         }else if(index == indexx){
    //             frontplayers.push(ite);
    //             frontplayers.push(item);
    //         }else if(index != indexq){
    //             frontplayers.push(item);
    //         }
    //     })
    //     players = frontplayers;
    // })
    // return players;

    ////4번째 시도================================================================속상쓰..
    // callings.forEach(cai => {
    //     let farr = [];
    //     for (let i = 1; i < players.length; i++) {
    //         if( players[i] == cai){
    //             farr.push(cai, players[i-1]);
    //             i++;
    //         }else{
    //             farr.push(players[i-1]);
    //         }
    //         if(i+1 == players.length){
    //             farr.push(players[i]);
    //         }
    //     }
    //     players = farr;
    // });
    // return players;

    ///다섯번째 시도.....
    let counters = {};
    callings.forEach(i => {
        if(counters[i] == undefined){
            counters[i] = 1;
        }else{
            counters[i] += 1;
        }
    });
    Object.keys(counters).forEach((cai)=>{
        console.log(cai, counters[cai])
        let farr = [];
        for (let i = counters[cai]; i < players.length; i++) {
            if( players[i] == cai){
                farr.push(cai, players[i-1]);
                //여기서 찾으면 행동할걸 적어줘야해
                i+= counters[cai];
            }else{
                farr.push(players[i-1]);
            }
        }
        players = farr;
    });
}
console.log(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]));