using System.ComponentModel.DataAnnotations;

namespace API.Entities
{
    public class AccountInfo
    {
        [Key]
        public int custID { get; set; }
        public string accountName { get; set; }
        public int accountNumber { get; set; }
        public int availableBal { get; set; }
    }
} 