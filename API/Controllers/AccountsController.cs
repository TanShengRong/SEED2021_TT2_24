using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using API.Data;
using API.DTOS;
using API.Entities;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace API.Controllers
{
    [ApiController]
    [Route("techtrek2020/[controller]")]
    public class AccountsController : ControllerBase
    {
        private readonly DataContext _context;
        public AccountsController(DataContext context)
        {
            _context = context;
        }


        [HttpGet("view")]
        public async Task<ActionResult<AccountInfo>> GetAccountInfo(accountDto accountDto)
        {
            return await _context.AccountInfos.FindAsync(accountDto.custID);
        }
    }
}  