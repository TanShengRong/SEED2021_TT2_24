using API.Entities;
using Microsoft.EntityFrameworkCore;
namespace API.Data
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions options) : base(options)
        {
        }
        public DbSet<LoginCredential> LoginCredentials { get; set; }
        public DbSet<AccountInfo> AccountInfos { get; set; }
    }
}  