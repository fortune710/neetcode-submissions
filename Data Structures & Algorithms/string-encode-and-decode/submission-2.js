class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map((str) => `${str.length}#${str}`).join('')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0;
        let res = [];

        while (i < str.length) {
            let j = i;

            while (str[j] !== "#") { j++ }

            let stringLength = parseInt(str.substring(i, j), 10);
            let newStr = str.substring(j + 1, j + 1 + stringLength);

            res.push(newStr)

            i = j + 1 + stringLength;
            j = i
        }

        return res
    }
}
