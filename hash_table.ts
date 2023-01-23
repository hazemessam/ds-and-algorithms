class LinkedListNode {
    key: string;
    val: string;
    next: LinkedListNode | null = null;

    constructor(key: string, val: any) {
        this.key = key;
        this.val = val;
    }

    toString(): string {
        return `{ key: ${this.key}, val: ${this.val}, next: ${this.next ? "Node" : null} }`;
    }
}


class LinkedList {
    private head: LinkedListNode | null = null;

    insert(key: string, val: any): void {
        const newNode = new LinkedListNode(key, val);
        newNode.next = this.head;
        this.head = newNode;
    }

    has(key: string): boolean {
        let cur = this.head;
        while (cur) {
            if (cur.key === key) return true;
            cur = cur.next;
        }
        return false;
    }

    get(key: string): any {
        let cur = this.head;
        while (cur) {
            if (cur.key === key) return cur.val;
            cur = cur.next;
        }
        throw Error(`The key ${key} doesn't exist`);
    }

    set(key: string, val: any): boolean {
        let cur = this.head;
        while (cur) {
            if (cur.key === key) {
                cur.val = val;
                return true;
            }
            cur = cur.next;
        }
        return false;
    }

    toString(): string {
        let cur = this.head;
        const nodes = Array<LinkedListNode>();
        while (cur) {
            nodes.push(cur);
            cur = cur.next;
        }
        return nodes.join(" -> ");
    }
}


class HashTable {
    private arr: Array<LinkedList>;

    constructor(size: number = 1024) {
        this.arr = new Array<LinkedList>(size);
    }

    private hashKey(key: string): number {
        const unicodeSum = key.split("").reduce((acc, cur, idx) => acc + cur.charCodeAt(0) * (idx + 1), 0);
        return unicodeSum % this.arr.length;
    }

    set(key: string, val: any): void {
        const idx = this.hashKey(key);
        if (!this.arr[idx]) this.arr[idx] = new LinkedList();

        const lnkdLst = this.arr[idx];
        lnkdLst.has(key) ? lnkdLst.set(key, val) : lnkdLst.insert(key, val);
    }

    get(key: string): any {
        const idx = this.hashKey(key);
        const lnkdLst = this.arr[idx];
        if (!lnkdLst || !lnkdLst.has(key)) return undefined;

        return lnkdLst.get(key);
    }

    toString(): string {
        const outputLst = Array<string>();
        this.arr.forEach((lnkdlst, idx) => {
            if (lnkdlst) outputLst.push(`${idx}:  ${lnkdlst}`);
        });
        return outputLst.join("\n");
    }
}


const ht = new HashTable(8);
ht.set("Hazem", 22);
ht.set("Omar", 4);
ht.set("Omar", 5);
ht.set("Seif", 3);
ht.set("Yousf", 2);
console.log(ht.toString());
