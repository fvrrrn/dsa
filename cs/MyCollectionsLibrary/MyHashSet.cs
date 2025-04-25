using System;

namespace MyCollectionsLibrary
{
    public class MyHashSet<T>
    {
        private T[] array;
        private int capacity;
        private int multiplier;

        public T this[string key] { get => array[GetIndexFromKey(key)]; }
        public int Count { get; private set; }

        public MyHashSet() : this(17576, 2)
        {
        }

        public MyHashSet(int capacity, int multiplier)
        {
            array = new T[capacity];
            this.capacity = capacity;
            this.multiplier = multiplier;
            Count = 0;
        }

        private void Resize()
        {
            capacity *= multiplier;
            T[] newArray = new T[capacity];

            for (int i = 0; i < Count; i++)
            {
                if (array[i] != null)
                {
                    throw new NotImplementedException();
                }
            }
        }

        private int GetValueFromChar(char c)
        {
            return c - 97;
        }

        private int GetIndexFromKey(string key, int index, int left, int right)
        {
            int charValue = key[index] - 97;

            // если длина участка меньше или равна 26, 
            // т.е. мы можем прикинуть, куда можно определить букву...
            if ((right - left) <= 26)
            {
                // ... рассчитываем множитель, который далее будет использован для сжатия
                // т.к. букв 26, но участок может быть меньше 26
                // так, буква z может быть размещена в 15, если такова длина
                float multiplier = (right - left) * 1.0f / 26;

                // рассчитываем, где находится буква на (мб сжатом) участке
                // например: на участке с длиной 26, буква y находится на 25 месте
                int temp = (int)(charValue * multiplier);

                // прибавляем к левой границе
                return left + temp;
            }

            // но если длина больше той, в какой можно размещать букву...
            int tmp = (right - left) / 26;
            // массив делится на 26 участков
            // смотрим, в какой участок попадает текущая буква
            // например: a попадает в первый участок(нулевой), b во второй и т.д.
            // так, находим левую границу
            left += charValue * tmp;

            // левая граница + длина участка = правая граница
            right = left + tmp;

            // рекурсивно вызываем функцию
            return GetIndexFromKey(key, index + 1, left, right);
        }

        private int GetIndexFromKey(string key)
        {
            int i = 1;
            int l = array.Length;
            while (l > 26)
            {
                l /= 26;
                i++;
            }
            string s = "";
            for (int j = 0; j < i - key.Length; j++)
            {
                s += "a";
            }
            s += key;

            return GetIndexFromKey(s, 0, 0, array.Length);
        }

        public void Add(string key, T value)
        {
            array[GetIndexFromKey(key)] = value;
            Count++;
        }
    }
}
