// 変数がガーベージコレクタに回収されてもテンソルは回収されない
document.write("tf.memory().numTensors: ", tf.memory().numTensors, "<br>")
document.write("tf.memory().numBytes: ", tf.memory().numBytes, "<br>")

let speedy = tf.tensor([1,2,3])
speedy = null // 参照を削除

// ページ/サーバが更新されるまでずっと残る（メモリリークが発生）
document.write("tf.memory().numTensors: ", tf.memory().numTensors, "<br>")
document.write("tf.memory().numBytes: ", tf.memory().numBytes, "<br>")

// 破棄した後に変数から参照しようとすると（Uncaught Error: Tensor is disposed.）
let t = tf.tensor([1,2,2])
t.dispose()
// document.write("tf.dispose(), Then show variable: ", t, "<br>")

// tidy()を用いた自動クリーンアップの手段（処理のカプセル化）
let keeper, chaser, seeker, beater
tf.tidy(() => {
    keeper = tf.tensor([1,2,3])
    chaser = tf.tensor([1,2,3])
    seeker = tf.tensor([1,2,3])
    beater = tf.tensor([1,2,3])
    document.write("Inside tidy (tf.memory().numTensors): ", tf.memory().numTensors, "<br>")
    
    tf.keep(keeper) // テンソルを保護
    return chaser // returnされるテンソルは破棄されない
})

document.write("After tidy (tf.memory().numTensors): ", tf.memory().numTensors, "<br>")
// document.write(seeker, "<br>") // seeker was released, Then show the variable (Error: Tensor is disposed.)
// document.write(beater, "<br>") // beater was released, Then show the variable (Error: Tensor is disposed.)
keeper.dispose()
chaser.dispose()

document.write("After dispose (tf.memory().numTensors): ", tf.memory().numTensors, "<br>")
