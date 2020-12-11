using System.ComponentModel.DataAnnotations;

namespace API.Entities
{
    public class LoginCredential
    {
        [Key]
        public int custID { get; set; }
        public string username { get; set; }
        public string password { get; set; }
    }
}