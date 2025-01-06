using System;

namespace Lab02
{
    // Interface for attacer objects
    public interface IAtk
    {
        void Attack(Unit unit);
    }

    // Interface for movable objects
    public interface IMov
    {
        void Move(int newX, int newY);
    }

    // Base abstract class for all game objects
    public abstract class GameObj
    {
        public int Id { get; }
        public string Name { get; }
        public int X { get; protected set; }
        public int Y { get; protected set; }

        public GameObj(int id, string name, int x, int y)
        {
            Id = id;
            Name = name;
            X = x;
            Y = y;
        }
    }

    // Abstrack class for units (stats)
    public abstract class Unit : GameObj
    {
        public float Hp { get; protected set; }

        protected Unit(int id, string name, int x, int y, float hp)
            : base(id, name, x, y) // : base (xyz) - parent values
        {
            Hp = hp;
        }

        public bool IsAlive() => Hp > 0; // => lambda func

        public void ReceiveDamage(float damage)
        {
            Hp = Math.Max(Hp - damage, 0);
        }
    }

    // Archer class -> atk + mov
    public class Archer : Unit, IAtk, IMov
    {
        public Archer(int id, string name, int x, int y, float hp)
            : base(id, name, x, y, hp) { }

        public void Attack(Unit unit)
        {
            Console.WriteLine($"{Name} attacks {unit.Name}!");
            unit.ReceiveDamage(7); // base dmg
        }

        public void Move(int newX, int newY)
        {
            Console.WriteLine($"{Name} moves from ({X}, {Y}) to ({newX}, {newY})");
            X = newX;
            Y = newY;
        }
    }

    // Abstract class for buildings
    public abstract class Building : GameObj
    {
        public bool IsBuilt { get; protected set; }

        protected Building(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y)
        {
            IsBuilt = isBuilt;
        }
    }

    // Fort -> atk
    public class Fort : Building, IAtk
    {
        public Fort(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y, isBuilt) { }

        public void Attack(Unit unit)
        {
            Console.WriteLine($"{Name} attacks {unit.Name} with cannons!");
            unit.ReceiveDamage(20); // base dmg
        }
    }

    // ModileHouse -> atk
    public class MobileHouse : Building, IMov
    {
        public MobileHouse(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y, isBuilt) { }

        public void Move(int newX, int newY)
        {
            Console.WriteLine($"{Name} moves from ({X}, {Y}) to ({newX}, {newY})");
            X = newX;
            Y = newY;
        }
    }

    // test sequence
    public class Program
    {
        public static void Main()
        {
            Archer archer = new Archer(1, "Archer", 0, 0, 100);
            Fort fort = new Fort(2, "Fort", 5, 5, true);
            MobileHouse mobileHouse = new MobileHouse(3, "MovableHouse", 10, 10, true);

            // movement and attack test
            archer.Move(3, 3);
            fort.Attack(archer);
            mobileHouse.Move(6, 6);

            Console.WriteLine($"Archer hp: {archer.Hp}");
        }
    }
}