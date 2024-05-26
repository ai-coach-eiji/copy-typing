const snap = tf.tensor([1,2,3])
console.log(snap) // 内部のデータではなく、オブジェクトの構造のみ表示される

// dataId: {}
// dtype: "float32" // テンソルのデータ型
// id: 0
// isDisposedInternal: false // まだ破棄されていない
// kept: false
// rankType: "1" // テンソルの階数
// shape: [3] // テンソルの形状
// size: 3 // テンソルの長さ
// strides: []
// isDisposed: (...)
// rank: (...)
// [[Prototype]]: Object

const crackle = tf.tensor([3.141592])
crackle.print() // テンソルのprint()メソッドで、内部の実際の値がコンソールに表示される

// ただし、このメソッドは値を返さず、内部で値を直接 console.log に渡している
// 内部の実際の値を使用したければ、Javascript変数として取り出さなければいけない
const pop = tf.tensor([[1,2,3], [4,5,6]])
console.log("pop.arraySync(): ", pop.arraySync()) // 2Dテンソルの値が2D配列として返る
console.log("pop.dataSync(): ", pop.dataSync()) // 2Dテンソルが平坦化された一次元Float32Arrayになる