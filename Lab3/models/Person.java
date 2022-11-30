package course.springRestaurant.App.models;

import javax.persistence.*;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

@Entity
@Table(name = "Person")
public class Person {

    @Id
    @Column(name = "id", insertable = false)
    @GeneratedValue (strategy = GenerationType.IDENTITY)
    private int id;

    @NotEmpty(message = "First name should not be empty")
    @Size(min = 2, max = 100, message = "First name should be between 2 and 100 symbols")
    @Column(name = "first_name")
    private String firstName;

    @NotEmpty(message = "Last name should not be empty")
    @Size(min = 2, max = 100, message = "Last name should be between 2 and 100 symbols")
    @Column(name = "last_name")
    private String lastName;

    @Min(value= 15, message = "Age should be bigger than 15")
    @Column(name = "age")
    private int age;

    @NotEmpty(message = "Username should not be empty")
    @Size(min = 2, max = 100, message = "Username should be between 2 and 100 symbols")
    @Column(name = "username")
    private String username;

    @Size(min = 2, max = 200, message = "Password should be between 2 and 200 symbols")
    @Column(name = "password")
    private String password;

    @Column(name = "role", insertable = false)
    private String role;

    public Person() {

    }

    public Person(String firstName, String lastName, String username, int age, String password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.username = username;
        this.age = age;
        this.password = password;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
}
