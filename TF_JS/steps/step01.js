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