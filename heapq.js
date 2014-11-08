function toInt(x) { return x | 0; }

function heapq() {
    this.q = [];

    // our heap logic is based on 1-based indexing, so each of these
    // operations adds 1 to the 0-based index, computes the related node
    // as 1-based index, and then subtracts 1 to get back the 0-based index.
    // IE. `2*0` would *NOT* give us the left child's position of the root.
    //     But, `2*1 - 1` does. Likewise, `2*0 + 1` does *NOT* give us the
    //     right child's position, but `(2*1 + 1) - 1` does.
    this.leftchild  = function(i) { return (2*(i+1))-1; };
    this.rightchild = function(i) { return (2*(i+1)+1)-1; };
    this.parent     = function(i) { return toInt((i+1)/2)-1; };

    this.score      = function(i) { return this.q[i][1]; };

    this.swap = function(i, j) {
        var _t = this;
        var tmp = _t.q[i];
        _t.q[i] = _t.q[j];
        _t.q[j] = tmp;
    };

    this.upheapify = function(i){
        var _t = this;
        var p = _t.parent(i);
        while(p >= 0 && _t.score(p) > _t.score(i)){
            _t.swap(p, i);
            i = p;
            p = _t.parent(i);
        }
        return i;
    };

    this.push = function(val, score){
        if(score === undefined) { throw "Undefined score."; }
        var _t = this;
        _t.q.push([val, score]);
        _t.upheapify(_t.q.length-1);
    };

    this.downheapify = function(i){
        var _t = this;
        var minchild;
        var l, r;
        // console.log("downheapify: " + _t.q);
        while(i<_t.q.length){
            l = _t.leftchild(i);
            r = _t.rightchild(i);
            if(l >= _t.q.length){
                // we are at the bottom
                return i;
            }
            // console.log("l: " + l + " i: " + i);
            if(r >= _t.q.length){
                if (_t.score(l) < _t.score(i)){
                    _t.swap(i, l);
                    i = l;
                }else{
                    return i;
                }
            }
            // both left child and right child exist
            else{
                // find the smaller valued child and move it up
                // so the invariant still holds
                minchild = _t.score(l) < _t.score(r) ? l : r;
                if(_t.score(minchild) < _t.score(i)){
                    _t.swap(i, minchild);
                    i = minchild;
                }else{
                    // con't go any farther
                    return i;
                }
            }
        }
    };

    this.pop = function(){
        var _t = this;
        // swap the last and the first value, putting the smallest value
        // at the end of the array
        var l = _t.q.length;
        _t.swap(0, l-1);
        var val = _t.q.pop();
        _t.downheapify(0);
        return val;
    };
}

module.exports = heapq;
