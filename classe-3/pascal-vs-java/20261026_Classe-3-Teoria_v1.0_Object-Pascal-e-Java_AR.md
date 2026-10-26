# مقارنة بين Object Pascal و Java

لماذا نتعلّم أسرع مع Object Pascal (Lazarus): كود أقل، متغيّرات بدون «new»، نوافذ نرسمها بالفأرة

الصف الثالث · 26/10/2026 · Versione 1.0

نفس البرنامج مكتوب بلغتين. انظر كم سطرًا نحتاج وكم كلمة جديدة يجب أن تتعلّم: ستفهم لماذا نبدأ بـ Lazarus. الكود يبقى بالحروف اللاتينية.

## 01 لغتان

**Object Pascal** هي لغة **Lazarus** (و Delphi). **Java** لغة مستعملة كثيرًا في الشركات وفي تطبيقات Android.

|  | Object Pascal (Lazarus) | Java |
|---|---|---|
| كيف يصبح برنامجًا | يُترجم (compilato): يصبح ملف .exe | يُترجم إلى «bytecode» ثم تفسّره آلة Java الافتراضية |
| ماذا نحتاج على الحاسوب | لا شيء: ملف .exe يعمل وحده | Java مثبّتة (الآلة الافتراضية) |
| النوافذ | ترسمها بالفأرة | تكتبها بالكود |

## 02 Hello World

**Object Pascal**

```
begin
  writeln('Hello World');
end.
```

**Java**

```
public class Ciao {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

في Java، لكتابة جملة واحدة فقط نحتاج **class** و **main** وكلمات مثل **public** و **static** و **void** و **String[] args**. في Object Pascal يكفي **begin** و **end**.

## 03 المتغيّرات: بدون «new»

في Object Pascal نُعلن المتغيّرات في قسم **var** بالاسم والنوع، ثم نستعملها مباشرة. حتى المصفوفة (array) جاهزة.

**Object Pascal**

```
var
  nome: string;
  eta: integer;
  voti: array[1..5] of integer;
begin
  nome := 'Ali';
  eta := 16;
  voti[1] := 8;
  readln(nome);        // leggo dalla tastiera
end.
```

في Java الأنواع البسيطة (int، double) لا مشكلة فيها، لكن للمصفوفة أو للقراءة من لوحة المفاتيح يجب **إنشاء كائن** بكلمة **new**.

**Java**

```
String nome = "Ali";
int eta = 16;
int[] voti = new int[5];          // serve new
voti[0] = 8;                       // si parte da 0
Scanner tastiera = new Scanner(System.in);   // serve new
nome = tastiera.nextLine();
```

> **اعرف هذا.** في Java المصفوفة تبدأ من 0؛ في Pascal تختار أنت أين تبدأ (هنا من 1). في Java كل شيء «كبير» يجب إنشاؤه بـ new قبل استعماله.

## 04 نافذة فيها زر

مع Lazarus تسحب الزر إلى النموذج (Form)، تضغط مرتين وتكتب **سطرًا واحدًا**:

**Object Pascal (Lazarus)**

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello World');
end;
```

في Java (مع Swing) النافذة والزر يُكتبان كلّهما بالكود، وكل واحد يُنشأ بـ **new**:

**Java**

```
JFrame finestra = new JFrame("Ciao");
JButton bottone = new JButton("Premi");
bottone.addActionListener(e ->
    JOptionPane.showMessageDialog(null, "Hello World"));
finestra.add(bottone);
finestra.setSize(300, 200);
finestra.setVisible(true);
```

## 05 الخلاصة

| ماذا | Object Pascal | Java |
|---|---|---|
| Hello World | سطر واحد داخل begin…end | 5 أسطر مع class و main |
| المتغيّرات والمصفوفات | في قسم var، جاهزة فورًا | المصفوفات وكائنات كثيرة بـ new |
| القراءة من لوحة المفاتيح | readln | new Scanner(System.in) |
| النوافذ والأزرار | نرسمها بالفأرة | نكتبها بالكود و new |
| البرنامج النهائي | ملف .exe يعمل في كل مكان | نحتاج Java مثبّتة |

## 06 لنكن صادقين

حتى في Object Pascal، **الأصناف** الأكثر تعقيدًا تُنشأ (**Create**) ثم تُحرَّر (**Free**). أمّا Java فتحرّر الذاكرة وحدها. و Java مستعملة كثيرًا في العمل: لهذا من الجيد أن نعرف أنها موجودة.

**Object Pascal**

```
var lista: TStringList;
begin
  lista := TStringList.Create;   // anche qui si crea
  lista.Add('Ali');
  lista.Free;                    // e si libera
end;
```

> **اعرف هذا.** لكن لتتعلّم البرمجة وترى النتيجة فورًا، Object Pascal مع Lazarus هي الطريق الأسهل: كلمات أقل، نوافذ بالفأرة، ملف .exe يعمل في كل مكان.

## 07 جرّب بنفسك

1. كم سطرًا نحتاج لـ Hello World في Object Pascal وكم في Java؟
2. في Java، ماذا نحتاج لإنشاء مصفوفة من 5 أرقام؟
3. لماذا يعمل برنامج Lazarus على كل حاسوب Windows بدون تثبيت أي شيء؟

### الحلول

1. Object Pascal: سطر واحد (داخل begin…end). Java: 5 أسطر مع class و main.
2. كلمة new: int[] voti = new int[5];
3. لأنه يُترجم إلى ملف .exe؛ أمّا Java فتحتاج آلتها الافتراضية مثبّتة.
