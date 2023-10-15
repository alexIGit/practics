class ArrayIterator {
	constructor(el) {
		this.index = 0;
		this.elements = el;
	}

	next() {
		return this.elements[this.index++];
	}

	hasNext() {
		return this.index < this.elements.length;
	}
};

class ObjectIterator {
	constructor(el) {
		this.index = 0;
		this.keys = Object.keys(el),
		this.elements = el;
	}

	next() {
		return this.elements[this.keys[this.index++]];
	}

	hasNext() {
		return this.index < this.keys.length;
	}
};


// --
const collection = new ArrayIterator(['audi', 'bmw', 'tesla']);
while(collection.hasNext()) {
    console.log(collection.next());
}

const autos = {
    audi: {model:'audi', color: 'black'},
    bmw: {model:'bmw', color: 'red'},
    tesla: {model:'tesla', color: 'blue'}
}
const collectionObj = new ObjectIterator(autos)
while(collectionObj.hasNext()) {
    console.log(collectionObj.next());
}