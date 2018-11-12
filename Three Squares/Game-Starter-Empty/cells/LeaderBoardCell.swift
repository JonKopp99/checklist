//
//  LeaderBoardCell.swift
//  Game-Starter-Empty
//
//  Created by Jonathan Kopp on 10/1/18.
//  Copyright © 2018 Make School. All rights reserved.
//

import Foundation
import UIKit

class LeaderBoardCell: UITableViewCell {
    //@IBOutlet weak var userImage: UIImageView!
    //@IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var scoreLabel: UILabel!
    
    
    
    override func layoutSubviews() {
        let huh = frame.width / 2
        //self.scoreLabel.frame = CGRect(x: 5, y: 5, width: 100, height: 50)
        self.nameLabel.frame = CGRect(x: huh, y: 20, width: 200, height: 20)
        nameLabel.font = UIFont(name: "Avenir Next Demi Bold", size: 21)
        self.nameLabel.sizeToFit()
    }
    //yes this is the one...
    
}
