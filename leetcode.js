// Merge 2 sorted arrays into one without using any type of sorting

let a = [1,4,5,5,9];
let b = [0,5,5,6,7,8];
let abLen = a.length + b.length;
let c = [];
let i = 0;
let idx;

while(true){
  if (b[i] <= a[i]) {
    c.push(b[i]);
    idx = b.indexOf(b[i]);
    b.splice(idx, 1);
  } else if (a[i] < b[i]) {
    c.push(a[i]);
    idx = a.indexOf(a[i]);
    a.splice(idx, 1);
  } else if (a.length == 0) {
    c.push(b[i]);
    idx = b.indexOf(b[i]);
    b.splice(idx, 1);
  } else if (b.length == 0) {
    c.push(a[i]);
    idx = a.indexOf(a[i]);
    a.splice(idx, 1);
  }

  if (abLen == c.length) {
    break;
  }
}

console.log(c);

// https://leetcode.com/problems/game-of-life/ MEDIUM #TODO
let board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
let boardObj = {};

function hasNeighbour (board, column, row) {
    try {
        board[column][row];
        return true;
      } catch {
        return false;
      }
}

function hasLiveNeighbour (neighbours) {
    let liveCheck = 0;
    for (let i = 0; i < neighbours.length; i++) {
        if (neighbours[i] == 1) { liveCheck++ }
    }
    return liveCheck;
}

function gameOfLife (board) {
    for (let y = 0; y < board.length; y++) {
        for (let x = 0; x < board[y].length; x++) {
            let cell = board[y][x];
            let neighbours = [];
            let liveNeighbours = 0;

            if (hasNeighbour(board,[y],[x-1])) { neighbours.push(board[y][x-1]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y],[x+1])) { neighbours.push(board[y][x+1]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y-1],[x-1])) { neighbours.push(board[y-1][x-1]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y-1],[x])) { neighbours.push(board[y-1][x]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y-1],[x+1])) { neighbours.push(board[y-1][x+1]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y+1],[x-1])) { neighbours.push(board[y+1][x-1]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y+1],[x])) { neighbours.push(board[y+1][x]) } else { neighbours.push(-1) }
            if (hasNeighbour(board,[y+1],[x+1])) { neighbours.push(board[y+1][x+1]) } else { neighbours.push(-1) }

            liveNeighbours = hasLiveNeighbour(neighbours);
            
            // Any live cell with fewer than two live neighbors dies as if caused by under-population.
            if (cell == 1 && liveNeighbours < 2) { boardObj[`${y},${x}`] = 0 }
            // Any live cell with two or three live neighbors lives on to the next generation.
            if (cell == 1 && liveNeighbours == 2) { boardObj[`${y},${x}`] = 1 }
            if (cell == 1 && liveNeighbours == 3) { boardObj[`${y},${x}`] = 1 }
            // Any live cell with more than three live neighbors dies, as if by over-population.
            if (cell == 1 && liveNeighbours > 3) { boardObj[`${y},${x}`] = 0 }
            // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if (cell == 0 && liveNeighbours == 3) { boardObj[`${y},${x}`] = 1 }

            console.log(`cell = ${cell}`);
            console.log(`neighbours = ${neighbours}`);
            console.log(`liveNeighbours = ${liveNeighbours}`);
        }
    }

    console.log(`boardObj = ${Object.entries(boardObj)}`);

    Object.entries(boardObj).forEach((entry) => {
        board[entry[0].charAt(0)][entry[0].charAt(2)] = entry[1];
    });

    return board;
}

// https://leetcode.com/problems/merge-sorted-array/ EASY

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

var merge = function (nums1, m, nums2, n) {
    if (n > 0) {
        if (m > 0) {
            for (i = 0; i < nums2.length; i++) {
                nums1[i + m] = nums2[i];
            }
        } else {
            for (i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
        }
    }
    nums1.sort(function(a, b) { return a - b });
};
