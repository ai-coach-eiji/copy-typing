const dataArray = [1, 1, 6, 1, 1, 3, 4, 1]
const first = tf.tensor(dataArray) // 配列の内容と構造は保持される
document.write("tf.tensor: ", first, "<br>")

const second = tf.tensor1d(dataArray) // 引数の次元をチェックできる（次元を保証できるのは6dまで）
document.write("tf.tensor1d: ", second, "<br>")

// テンソルのデータ型は一様でなければいけない
const dataF = tf.tensor([1.1, 2.2, 3.3])
document.write("<br>", "tf.tensor([1.1, 2.2, 3.3]) Data type: ", dataF.dtype, "<br>") // 浮動小数点の場合はデフォルトでfloat32で値が保持される
// int32
const dataI = tf.tensor([1, 2, 3], null, 'int32') // 第三引数でデータの型を指定
document.write("tf.tensor([1, 2, 3], null, 'int32') Data type: ", dataI.dtype, "<br>")
// bool
const dataB = tf.tensor([true, true, false])
document.write("tf.tensor([true, true, false]) Data type: ", dataB.dtype, "<br>")
// int32
const dataI2 = tf.tensor([true, true, false], null, "int32") // int32を指定すると、falseは0に、trueは1にキャストされる
document.write("tf.tensor([true, true, false], null, 'int32') Data type: ", dataI2.dtype, "<br>")
// Size
document.write("tf.tensor([true, true, false]) Size: ", dataI2.size, "<br>")
// 一次元の入力配列を二次元のテンソルに変換
const d = tf.tensor([1,1,0,1,1,1,0,0,1], [3,3], 'int32') // 数値として安心なのはデフォルトのfloat32（int32は、丸めて保持してもかまわない時に使う）
document.write("tf.tensor([1,1,0,1,1,1,0,0,1], [3,3], 'int32'): ", d, "<br>")
// 新しい型のテンソルを作成
const nope = tf.tensor([1.1,1,0,1,1,1,0,0,1])
const y = nope.asType('int32') // ただし、あまり賢い方法ではない（小数点以下を取り除くだけで、正しい四捨五入ではない）
document.write("tf.tensor([1.1,1,0,1,1,1,0,0,1]).asType('float32'): ", y.dtype, "<br>")