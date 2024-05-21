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