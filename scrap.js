
            if(!l){
                // we are at the bottom
                return i;
            }
            // if the right child is undefined
            else if(!r && _t.score(l) < _t.score(i)){
                _t.swap(i, l);
                i = l;
            }

        /*
        // first, make all the original edges possible for each spot
        // via a roll of the dice.
        for(j=1; j<=100; j++){
            // make an edge from each node to the 6 nodes ahead.
            a = j;
            if(edges[a] === undefined){ edges[a] = []; }
            for(b=a+1; b<=a+6; b++){
                if(b > 100) { break; }
                edges[a].push(b);
            }
        }
       */

    /*
     * player = 1 for me, 2 for other.
     * call function again with the new array with our selections taken
     * return player 1's accumulated score always
     */
    // var newArr = arr.slice(mini);
