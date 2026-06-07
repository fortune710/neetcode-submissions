class MinStack {
    constructor() {}

    //A regular stack to keep all the items in no order
    stack = [];

    //A stack to keep all the minimum values in the regaular stack
    minStack = [];

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        //If the stack for tracking minimums is empty or the item to be pushed 
        //is elss than the item at the end of the min stack, we push to min stack
        if (this.minStack.length === 0 || val <= this.minStack.at(-1)) {
            this.minStack.push(val)
        }
        
        this.stack.push(val)
    }

    /**
     * @return {void}
     */
    pop() {
        //If the item at the top of the regular stack is currently the minimum in the stack
        //We pop from min stack to give us te next minumum
        if (this.stack.at(-1) === this.minStack.at(-1)) {
            this.minStack.pop()
        }
        
        this.stack.pop()
    }

    /**
     * @return {number}
     */
    top() {
        if (this.stack.length > 0) return this.stack.at(-1)
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack.at(-1)
    }
}
