import java.util.*;
class IAttack {
    void showAttack() {}; }
class CSpider extends IAttack {
    public void showAttack() {
        System.out.println("蜘蛛人的攻擊力：60");
        System.out.println("攻擊方式會發射蜘蛛網！\n");  }  }
class CSuperMan extends IAttack {
    public void showAttack() {
        System.out.println("超人的攻擊力：100");
        System.out.println("攻擊方式使用拳頭！\n"); } }
public class MyTest4 {
    public static void main(String[] args) {
        IAttack flag;
        CSpider Bill = new CSpider();
        CSuperMan clark = new CSuperMan();
        flag = Bill;
        flag.showAttack();
        flag = clark;
        flag.showAttack(); } }

