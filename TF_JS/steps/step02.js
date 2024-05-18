// 変数がガーベージコレクタに回収されてもテンソルは回収されない
document.write("tf.memory().numTensors: ", tf.memory().numTensors, "<br>")
document.write("tf.memory().numBytes: ", tf.memory().numBytes, "<br>")

let speedy = tf.tensor([1,2,3])
speedy = null // 参照を削除

// ページ/サーバが更新されるまでずっと残る
document.write("tf.memory().numTensors: ", tf.memory().numTensors, "<br>")
document.write("tf.memory().numBytes: ", tf.memory().numBytes, "<br>")

