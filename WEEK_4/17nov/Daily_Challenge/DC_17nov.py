title = "<h1>MY SIMPLE CV BY PYTHON</h1>"
profil = "<img src=""profil.jpg"" alt=""Smiley face"" height=""100"" width=""100"">"
fn = input("Give your fullname: ")
full_name = "<div><label>Full Name: </label><p>%s</p></div>" % (fn)
bd = input("Enter your complete birthday: ")
birthday = "<p><label>Birthday: </label>%s</p>" % (bd)
jb = input("What is/are your actual job(s): ")
job = "<p><label>Job&Background: </label>%s</p>" % (jb)
psnl = input("What is your personality? ")
personality = "<p><label>Personality: </label>%s/p>" % (psnl)
ct = input("How can we contact you? ")
contact = "<div><label>Contact: </label>%s</div>" % (ct)


print("%s\n\n%s\n%s\n%s\n%s\n%s\n%s\n" % (title, profil, full_name, birthday, job, personality,contact))